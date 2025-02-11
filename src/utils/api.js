export const API_URL = "http://127.0.0.1:5000/api";

export const fetchWithAuth = async (url, options = {}) => {
    const token = localStorage.getItem("token");
    return fetch(`${API_URL}${url}`, {
        ...options,
        headers: {
            "Content-Type": "application/json",
            Authorization: token ? `Bearer ${token}` : "",
        },
    });
};
