import { RestfulProvider } from '../restful_provider';
import type { RequestParams, GetListResponse, RequestBody, GetDetailsResponse } from '../../types/index';

export class CrudProvider {
    restfulProvider = new RestfulProvider()
    async get_list(entity: string, params: RequestParams = undefined){
        return new Promise<GetListResponse>((resolve, reject) => {
            this.restfulProvider.get(import.meta.env.VITE_BASE_URL, entity, params, {})
            .then((response) => {
                let data: GetListResponse = {
                    pagination: {
                        current: response.data.current,
                        next: response.data.next,
                        previous: response.data.previous,
                        has_next: response.data.has_next,
                        has_previous: response.data.has_previous
                    },
                    data: []
                }
                resolve(data); 
            })
            .catch((error) => {
                reject(error);
            });
        })
    }

    async get_details(entity: string, id: string | number, params: RequestParams = undefined){
        return new Promise((resolve, reject) => {
            this.restfulProvider.get(import.meta.env.VITE_BASE_URL, entity, params, {}, id)
            .then((response) => {
                let data: GetDetailsResponse = {...response.data}
               resolve(data); 
            })
            .catch((error) => {
                reject(error);
            });
        })
    }

    async create(entity: string, body: RequestBody){
        return new Promise((resolve, reject) => {
            this.restfulProvider.post(import.meta.env.VITE_BASE_URL, entity, body)
            .then((response) => {
               resolve(response); 
            })
            .catch((error) => {
                reject(error);
            });
        })
    }

    async update(entity: string, id: string, body: RequestBody){
        return new Promise((resolve, reject) => {
            this.restfulProvider.put(import.meta.env.VITE_BASE_URL, entity, id, body)
            .then((response) => {
               resolve(response); 
            })
            .catch((error) => {
                reject(error);
            });
        })
    }

    async remove(entity: string, id: string){
        return new Promise((resolve, reject) => {
            this.restfulProvider.delete(import.meta.env.VITE_BASE_URL, entity, id)
            .then((response) => {
               resolve(response); 
            })
            .catch((error) => {
                reject(error);
            });
        })
    }
}