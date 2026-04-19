// src/utils/api.ts

export async function fetchStories() {
  const res = await fetch("http://localhost:8000/api/v1/stories/active");
  return res.json();
}

export async function fetchVideos() {
  const res = await fetch("http://localhost:8000/api/v1/videos/feed");
  return res.json();
}