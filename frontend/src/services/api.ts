const API_URL = "http://127.0.0.1:5000";

export const getDashboardSummary = async () => {
  const response = await fetch(`${API_URL}/api/dashboard-summary`);
  return response.json();
};