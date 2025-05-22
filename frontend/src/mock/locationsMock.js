// Mock data for locations
export const mockLocations = [
  {
    id: '1',
    name: 'Riga Office',
    description: 'Main headquarters',
    coordinates: [24.1052, 56.9496],
    state: 'active',
    metadata: {
      address: 'Central District, Riga, Latvia',
      type: 'headquarters'
    },
    createdAt: new Date('2023-01-01'),
    updatedAt: new Date('2023-06-15')
  },
  {
    id: '2',
    name: 'Ventspils Branch',
    description: 'Western regional office',
    coordinates: [21.5584, 57.3961],
    state: 'warning',
    metadata: {
      address: 'Ventspils, Latvia',
      type: 'regional'
    },
    createdAt: new Date('2023-02-10'),
    updatedAt: new Date('2023-08-22')
  },
  {
    id: '3',
    name: 'Daugavpils Branch',
    description: 'Eastern regional office',
    coordinates: [26.5341, 55.8739],
    state: 'error',
    metadata: {
      address: 'Daugavpils, Latvia',
      type: 'regional'
    },
    createdAt: new Date('2023-03-15'),
    updatedAt: new Date('2023-09-01')
  },
  {
    id: '4',
    name: 'Liepāja Branch',
    description: 'Southwest office',
    coordinates: [21.0107, 56.5047],
    state: 'inactive',
    metadata: {
      address: 'Liepāja, Latvia',
      type: 'regional'
    },
    createdAt: new Date('2023-04-20'),
    updatedAt: new Date('2023-07-12')
  },
  {
    id: '5',
    name: 'Jūrmala Office',
    description: 'Coastal regional office',
    coordinates: [23.7726, 56.9682],
    state: 'active',
    metadata: {
      address: 'Jūrmala, Latvia',
      type: 'regional'
    },
    createdAt: new Date('2023-05-05'),
    updatedAt: new Date('2023-09-30')
  }
];