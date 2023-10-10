import axios from "axios";

export const instance = axios.create({
  baseURL: "https://chemix-server.vercel.app/chem",
});

export default instance;