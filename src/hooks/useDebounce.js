import { useState, useEffect } from 'react';

/**
 * Custom hook untuk debouncing value
 * @param {*} value - Nilai yang akan di-debounce
 * @param {number} delay - Delay dalam milliseconds
 * @returns {*} - Debounced value
 */
export const useDebounce = (value, delay = 300) => {
  const [debouncedValue, setDebouncedValue] = useState(value);

  useEffect(() => {
    // Set timeout untuk update debounced value
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    // Cleanup function untuk clear timeout
    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
