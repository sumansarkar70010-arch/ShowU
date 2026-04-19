// src/components/VideoFeed.tsx

import { useEffect, useState } from "react";
import { fetchVideos } from "../utils/api";

export default function VideoFeed() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    fetchVideos().then(setVideos);
  }, []);

  return (
    <div className="video-feed">
      {videos.map((video: any) => (
        <video key={video.id} src={video.file_path} controls autoPlay loop />
      ))}
    </div>
  );
}