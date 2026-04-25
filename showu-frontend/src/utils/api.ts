// src/utils/api.ts

const BASE_URL = "https://showu.onrender.com/api/v1";

export async function fetchStories() {
  const res = await fetch(`${BASE_URL}/stories/active`);
  return res.json();
}

export async function fetchVideos() {
  const res = await fetch(`${BASE_URL}/videos/feed`);
  return res.json();
}