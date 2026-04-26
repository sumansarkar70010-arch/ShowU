// src/utils/api.ts

const BASE_URL = "https://showu.onrender.com/api/v1";

export async function fetchProtected(token: string) {
  const res = await fetch(`${BASE_URL}/users/me`, {
    headers: { Authorization: `Bearer ${token}` },
  });
  if (!res.ok) throw new Error("Unauthorized");
  return res.json();
}