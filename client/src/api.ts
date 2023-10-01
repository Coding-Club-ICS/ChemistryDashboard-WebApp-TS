import axios from "axios";

export const instance = axios.create({
  baseURL: "https://automatic-parakeet-x44xr9j757phqxq-5000.preview.app.github.dev/chem",
});

export default instance;