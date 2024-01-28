import axios from 'axios';

export class RestfulProvider {
    constructor(){
        axios.defaults.headers.common['authorization'] = `${localStorage.getItem('token')}`
    }

    async get(base_url: string, path: string, params: object = {}, headers: object = {}, id: string | number = ""): Promise<any> {
        
        const url = id != ""? `${base_url}/${path}/${id}` : `${base_url}/${path}`;

        return new Promise ((resolve, reject) => {
            axios.get(`${url}/${path}`, {params, headers})
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            })
        })
    }

    async post(base_url: string, path: string, body: object, params: object = {}, headers: object = {}): Promise<any> {
        return new Promise ((resolve, reject) => {
            axios.post(`${base_url}/${path}`, body, {params, headers})
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            })
        })
    }

    async put(base_url: string, path: string, id: string | number = "", body: object, params: object = {}, headers: object = {}): Promise<any> {
        return new Promise ((resolve, reject) => {
            const url = id != ""? `${base_url}/${path}/${id}` : `${base_url}/${path}`;

            axios.put(url, body, {params, headers})
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            })
        })
    }

    async delete(base_url: string, path: string, id: string | number = "", headers: object = {}): Promise<any> {
        return new Promise ((resolve, reject) => {
            const url = id != ""? `${base_url}/${path}/${id}` : `${base_url}/${path}`;

            axios.delete(url, {headers})
            .then((response) => {
                resolve(response);
            })
            .catch((error) => {
                reject(error);
            })
        })
    }
}