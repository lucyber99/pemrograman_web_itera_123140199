import { describe, it, expect, beforeEach } from 'vitest';
import { validateBookInput, generateId } from '../utils/validation';

describe('Validation Utils', () => {
  describe('validateBookInput', () => {
    it('should validate a valid book input', () => {
      const book = {
        title: 'Test Book',
        author: 'Test Author',
        status: 'milik'
      };

      const result = validateBookInput(book);

      expect(result.isValid).toBe(true);
      expect(result.errors).toEqual({});
    });

    it('should return error when title is empty', () => {
      const book = {
        title: '',
        author: 'Test Author',
        status: 'milik'
      };

      const result = validateBookInput(book);

      expect(result.isValid).toBe(false);
      expect(result.errors.title).toBeDefined();
    });

    it('should return error when title is too short', () => {
      const book = {
        title: 'A',
        author: 'Test Author',
        status: 'milik'
      };

      const result = validateBookInput(book);

      expect(result.isValid).toBe(false);
      expect(result.errors.title).toContain('minimal 2 karakter');
    });

    it('should return error when author is empty', () => {
      const book = {
        title: 'Test Book',
        author: '',
        status: 'milik'
      };

      const result = validateBookInput(book);

      expect(result.isValid).toBe(false);
      expect(result.errors.author).toBeDefined();
    });

    it('should return error when status is invalid', () => {
      const book = {
        title: 'Test Book',
        author: 'Test Author',
        status: 'invalid'
      };

      const result = validateBookInput(book);

      expect(result.isValid).toBe(false);
      expect(result.errors.status).toBeDefined();
    });

    it('should validate all three valid statuses', () => {
      const statuses = ['milik', 'baca', 'beli'];
      
      statuses.forEach(status => {
        const book = {
          title: 'Test Book',
          author: 'Test Author',
          status
        };

        const result = validateBookInput(book);
        expect(result.isValid).toBe(true);
      });
    });
  });

  describe('generateId', () => {
    it('should generate a unique ID', () => {
      const id1 = generateId();
      const id2 = generateId();

      expect(id1).toBeTruthy();
      expect(id2).toBeTruthy();
      expect(id1).not.toBe(id2);
    });

    it('should generate a string ID', () => {
      const id = generateId();
      expect(typeof id).toBe('string');
    });
  });
});
