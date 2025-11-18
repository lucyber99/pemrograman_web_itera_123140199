import { describe, it, expect } from 'vitest';
import { renderHook, waitFor } from '@testing-library/react';
import { useDebounce } from '../hooks/useDebounce';

describe('useDebounce Hook', () => {
  it('should return initial value immediately', () => {
    const { result } = renderHook(() => useDebounce('test', 300));
    
    expect(result.current).toBe('test');
  });

  it('should debounce value changes', async () => {
    const { result, rerender } = renderHook(
      ({ value, delay }) => useDebounce(value, delay),
      {
        initialProps: { value: 'initial', delay: 300 }
      }
    );
    
    expect(result.current).toBe('initial');
    
    // Update value
    rerender({ value: 'updated', delay: 300 });
    
    // Value tidak langsung berubah
    expect(result.current).toBe('initial');
    
    // Tunggu debounce delay
    await waitFor(() => {
      expect(result.current).toBe('updated');
    }, { timeout: 400 });
  });

  it('should cancel previous debounce on rapid changes', async () => {
    const { result, rerender } = renderHook(
      ({ value, delay }) => useDebounce(value, delay),
      {
        initialProps: { value: 'first', delay: 300 }
      }
    );
    
    // Rapid changes
    rerender({ value: 'second', delay: 300 });
    rerender({ value: 'third', delay: 300 });
    rerender({ value: 'fourth', delay: 300 });
    
    // Should still be initial value
    expect(result.current).toBe('first');
    
    // After delay, should be the last value
    await waitFor(() => {
      expect(result.current).toBe('fourth');
    }, { timeout: 400 });
  });

  it('should work with custom delay', async () => {
    const { result, rerender } = renderHook(
      ({ value, delay }) => useDebounce(value, delay),
      {
        initialProps: { value: 'initial', delay: 100 }
      }
    );
    
    rerender({ value: 'updated', delay: 100 });
    
    await waitFor(() => {
      expect(result.current).toBe('updated');
    }, { timeout: 200 });
  });
});
