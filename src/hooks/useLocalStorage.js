import { useState, useEffect } from 'react';

/**
 * Custom hook untuk mengelola state dengan localStorage
 * @param {string} key - Key untuk localStorage
 * @param {*} initialValue - Nilai awal jika tidak ada di localStorage
 * @returns {Array} - [storedValue, setValue]
 */
export const useLocalStorage = (key, initialValue) => {
  // State untuk menyimpan nilai
  const [storedValue, setStoredValue] = useState(() => {
    try {
      // Ambil dari localStorage
      const item = window.localStorage.getItem(key);
      // Parse dan return jika ada, jika tidak return initialValue
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error loading ${key} from localStorage:`, error);
      return initialValue;
    }
  });

  // Gunakan useEffect untuk update localStorage ketika value berubah
  useEffect(() => {
    try {
      window.localStorage.setItem(key, JSON.stringify(storedValue));
    } catch (error) {
      console.error(`Error saving ${key} to localStorage:`, error);
    }
  }, [key, storedValue]);

  return [storedValue, setStoredValue];
};
