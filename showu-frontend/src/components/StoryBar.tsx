import { useEffect, useState } from "react";
import { fetchStories } from "../utils/api";

interface Story {
  id: string;
  media_url: string;
}

export default function StoryBar() {
  const [stories, setStories] = useState<Story[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetchStories()
      .then(setStories)
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

  if (loading) return <div className="story-bar">Loading...</div>;
  if (error) return <div className="story-bar">Error: {error}</div>;

  return (
    <div className="story-bar">
      {stories.map((story) => (
        <div key={story.id} className="story">
          <img src={story.media_url} alt={`Story by ${story.id}`} />
        </div>
      ))}
    </div>
  );
}