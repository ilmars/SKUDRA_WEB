// Locations Vuex Module
import axios from 'axios'
import { mockLocations } from '@/mock/locationsMock'

// Default API endpoint, adjust as needed for your environment
const API_URL = '/api/sensors/instances/?receivers=false'
// const USE_MOCK = process.env.NODE_ENV === 'development'
const USE_MOCK = false 

export default {
    namespaced: true,

    state: () => ({
        list: [
            {
                "url": "http://localhost:8000/api/sensors/instances/5/",
                "id": 5,
                "ip": "10.0.50.102",
                "port": 19010,
                "driver_name": "Valmiera",
                "user_has_access": false,
                "state": "UNAVAILABLE",
                "location": null,
                "coordinates": [
                    null,
                    null
                ],
                "receivers": []
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/6/",
                "id": 6,
                "ip": "10.0.50.82",
                "port": 19010,
                "driver_name": "Rezekne",
                "user_has_access": false,
                "state": "UNAVAILABLE",
                "location": null,
                "coordinates": [
                    null,
                    null
                ],
                "receivers": []
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/1/",
                "id": 1,
                "ip": "10.0.50.162",
                "port": 19010,
                "driver_name": "Grobina",
                "user_has_access": false,
                "state": "READY",
                "location": "SRID=4326;POINT (21.077461111 56.501169444)",
                "coordinates": [
                    21.077461111,
                    56.501169444
                ],
                "receivers": [
                    "http://localhost:8000/api/sensors/receivers/13/",
                    "http://localhost:8000/api/sensors/receivers/14/",
                    "http://localhost:8000/api/sensors/receivers/15/"
                ]
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/9/",
                "id": 9,
                "ip": "10.0.50.42",
                "port": 19010,
                "driver_name": "Bauskas",
                "user_has_access": false,
                "state": "READY",
                "location": "SRID=4326;POINT (24.144138 56.9035557)",
                "coordinates": [
                    24.144138,
                    56.9035557
                ],
                "receivers": [
                    "http://localhost:8000/api/sensors/receivers/4/",
                    "http://localhost:8000/api/sensors/receivers/5/"
                ]
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/2/",
                "id": 2,
                "ip": "10.0.50.152",
                "port": 19010,
                "driver_name": "TMS",
                "user_has_access": false,
                "state": "READY",
                "location": "SRID=4326;POINT (26.291688888 55.976826111)",
                "coordinates": [
                    26.291688888,
                    55.976826111
                ],
                "receivers": [
                    "http://localhost:8000/api/sensors/receivers/11/",
                    "http://localhost:8000/api/sensors/receivers/12/"
                ]
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/4/",
                "id": 4,
                "ip": "10.0.50.122",
                "port": 19010,
                "driver_name": "Ventspils",
                "user_has_access": false,
                "state": "READY",
                "location": "SRID=4326;POINT (21.550003205 57.383245149)",
                "coordinates": [
                    21.550003205,
                    57.383245149
                ],
                "receivers": [
                    "http://localhost:8000/api/sensors/receivers/6/",
                    "http://localhost:8000/api/sensors/receivers/7/",
                    "http://localhost:8000/api/sensors/receivers/8/"
                ]
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/7/",
                "id": 7,
                "ip": "10.0.50.72",
                "port": 19010,
                "driver_name": "Daugavpils",
                "user_has_access": false,
                "state": "UNAVAILABLE",
                "location": null,
                "coordinates": [
                    null,
                    null
                ],
                "receivers": []
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/10/",
                "id": 10,
                "ip": "10.0.50.22",
                "port": 19010,
                "driver_name": "Ezermalas",
                "user_has_access": false,
                "state": "READY",
                "location": "SRID=4326;POINT (24.194582488 56.993955373)",
                "coordinates": [
                    24.194582488,
                    56.993955373
                ],
                "receivers": [
                    "http://localhost:8000/api/sensors/receivers/1/",
                    "http://localhost:8000/api/sensors/receivers/2/"
                ]
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/8/",
                "id": 8,
                "ip": "10.0.50.52",
                "port": 19010,
                "driver_name": "Sloka",
                "user_has_access": false,
                "state": "UNAVAILABLE",
                "location": null,
                "coordinates": [
                    null,
                    null
                ],
                "receivers": []
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/11/",
                "id": 11,
                "ip": "10.0.50.2",
                "port": 19010,
                "driver_name": "Perses",
                "user_has_access": false,
                "state": "UNAVAILABLE",
                "location": null,
                "coordinates": [
                    null,
                    null
                ],
                "receivers": []
            },
            {
                "url": "http://localhost:8000/api/sensors/instances/3/",
                "id": 3,
                "ip": "10.0.50.132",
                "port": 19010,
                "driver_name": "Metalurgs",
                "user_has_access": false,
                "state": "READY",
                "location": "SRID=4326;POINT (21.026833 56.524428)",
                "coordinates": [
                    21.026833,
                    56.524428
                ],
                "receivers": [
                    "http://localhost:8000/api/sensors/receivers/9/",
                    "http://localhost:8000/api/sensors/receivers/10/"
                ]
            }
        ],
        loading: false,
        error: null
    }),

    mutations: {
        SET_LOCATIONS(state, locations) {
            state.list = locations;
        },
        SET_LOADING(state, status) {
            state.loading = status;
        },
        SET_ERROR(state, error) {
            state.error = error;
        }
    },

    actions: {
        async fetchLocations({ commit }) {
            console.log('Fetching locations...')
            commit('SET_LOADING', true);
            let params = Object.assign({}, { page: 1, limit: 100 });
            try {
                // Normally you would fetch from API
                //     return axios
                // .get(url, {
                //   params: params
                // })
                // .then(response => (
                //   commit(obj.commitName, { ...response.data, ...obj }, { root: true })
                // ))
                // .catch(error => {
                //   commit('common/SET_ERROR', { error, routeModule: rootState.route }, { root: true })
                // });
                const mockLocations = [
                    {
                        "url": "http://localhost:8000/api/sensors/instances/9/",
                        "id": 9,
                        "ip": "10.0.50.42",
                        "port": 19010,
                        "driver_name": "Bauskas",
                        "user_has_access": false,
                        "state": "READY",
                        "location": "SRID=4326;POINT (24.144138 56.9035557)",
                        "coordinates": [
                            24.144138,
                            56.9035557
                        ],
                        "receivers": [
                            {
                                "guid": "294f9c6a-0c07-4982-9d31-2e7eaf08a550",
                                "name": "SignalShark",
                                "state": "READY",
                                "type": "",
                                "sensor_id": 9
                            },
                            {
                                "guid": "3dd99d42-02db-4339-bb91-de49e9156192",
                                "name": "DDF225",
                                "state": "READY",
                                "type": "DDF255",
                                "sensor_id": 9
                            }
                        ]
                    },
                    
                ];
                console.warn('use fn fetchLocations', USE_MOCK)
                if (USE_MOCK) {
                    // Use mock data in development
                    commit('SET_LOCATIONS', mockLocations);
                } else {
                    console.log('before axios.get', API_URL)
                    // Use real API endpoint in production
                    try {
                        const response = await axios.get(API_URL, {params: params});
                        // Extract data from the 'results' key in the response
                        const locations = response.data || [];
                        commit('SET_LOCATIONS', locations);
                    } catch (error) {
                        console.error('API Error:', error);
                        commit('SET_ERROR', error.message || 'Failed to fetch locations');
                        throw error;
                    }
                }

                // For now, just use default data
                

                // commit('SET_LOCATIONS', data);
                commit('SET_ERROR', null);
            } catch (error) {
                console.error('Error fetching locations:', error);
                commit('SET_ERROR', 'Failed to fetch locations');
                commit('SET_LOCATIONS', []);
            } finally {
                commit('SET_LOADING', false);
            }
        }
    },

    getters: {
        allLocations: state => state.list,
        isLoading: state => state.loading,
        hasError: state => !!state.error
    }
}