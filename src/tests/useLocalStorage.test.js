import { describe, it, expect, beforeEach, vi } from 'vitest';
import { renderHook, act } from '@testing-library/react';
import { useLocalStorage } from '../hooks/useLocalStorage';

describe('useLocalStorage Hook', () => {
  beforeEach(() => {
    // Clear localStorage sebelum setiap test
    localStorage.clear();
  });

  it('should initialize with initial value when localStorage is empty', () => {
    const { result } = renderHook(() => useLocalStorage('testKey', 'initialValue'));
    
    expect(result.current[0]).toBe('initialValue');
  });

  it('should initialize with value from localStorage if exists', () => {
    localStorage.setItem('testKey', JSON.stringify('storedValue'));
    
    const { result } = renderHook(() => useLocalStorage('testKey', 'initialValue'));
    
    expect(result.current[0]).toBe('storedValue');
  });

  it('should update localStorage when value changes', () => {
    const { result } = renderHook(() => useLocalStorage('testKey', 'initialValue'));
    
    act(() => {
      result.current[1]('newValue');
    });
    
    expect(result.current[0]).toBe('newValue');
    expect(localStorage.getItem('testKey')).toBe(JSON.stringify('newValue'));
  });

  it('should handle objects and arrays', () => {
    const initialArray = [{ id: 1, name: 'Test' }];
    const { result } = renderHook(() => useLocalStorage('testKey', initialArray));
    
    expect(result.current[0]).toEqual(initialArray);
    
    const newArray = [{ id: 1, name: 'Test' }, { id: 2, name: 'Test 2' }];
    act(() => {
      result.current[1](newArray);
    });
    
    expect(result.current[0]).toEqual(newArray);
    expect(JSON.parse(localStorage.getItem('testKey'))).toEqual(newArray);
  });

  it('should handle invalid JSON in localStorage gracefully', () => {
    localStorage.setItem('testKey', 'invalid json');
    
    const { result } = renderHook(() => useLocalStorage('testKey', 'fallback'));
    
    expect(result.current[0]).toBe('fallback');
  });
});
