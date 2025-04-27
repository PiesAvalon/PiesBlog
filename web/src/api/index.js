import axios from 'axios';

const api = axios.create({
  baseURL: 'http://localhost:8000', // FastAPI默认端口
  headers: {
    'Accept': 'application/json'
  }
});

export const getRoot = async () => {
  return api.get('/');
};