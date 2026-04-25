// src/pages/profile/[id].tsx

import { useContext, useEffect, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import { useRouter } from "next/router";

export default function ProfilePage() {
  // ১. Context কল করার সময় একটি ডিফেন্সিভ চেক (Default value) যোগ করা হয়েছে
  const authContext = useContext(AuthContext);
  const token = authContext ? authContext.token : null;
  
  const router = useRouter();
  const { id } = router.query;
  const [profile, setProfile] = useState<any>(null);

  useEffect(() => {
    // ২. বিল্ড টাইমে যেন কোডটি রান না করে সেজন্য window চেক
    if (typeof window === "undefined") return;

    if (!token) {
      router.push("/login");
      return;
    }
    
    if (id) {
      fetch(`http://localhost:8000/api/v1/users/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      })
        .then(res => res.json())
        .then(setProfile)
        .catch(err => console.error("Fetch error:", err));
    }
  }, [id, token, router]);

  if (!profile) return <p>Loading...</p>;

  return (
    <div>
      <h2>{profile.username}</h2>
      <p>{profile.email}</p>
    </div>
  );
}