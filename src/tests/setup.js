import { expect, afterEach } from 'vitest';
import { cleanup } from '@testing-library/react';
import '@testing-library/jest-dom';

// Cleanup setelah setiap test
afterEach(() => {
  cleanup();
});
