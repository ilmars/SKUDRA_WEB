/**
 * Location data interface
 * 
 * @typedef {Object} Location
 * @property {string} id - Unique identifier for the location
 * @property {string} name - Name of the location
 * @property {string} [description] - Optional description of the location
 * @property {number[]} coordinates - [longitude, latitude] coordinates
 * @property {string} state - Status state of the location ('active', 'warning', 'error', 'inactive')
 * @property {Object} [metadata] - Optional additional metadata
 * @property {Date} [createdAt] - Creation timestamp
 * @property {Date} [updatedAt] - Last update timestamp
 */

// This file serves as documentation for the Location data structure
// used throughout the application