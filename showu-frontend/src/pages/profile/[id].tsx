// src/pages/profile/[id].tsx

import { useContext, useEffect, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import { useRouter } from "next/router";

export default function ProfilePage() {
  const context = useContext(AuthContext);
  const router = useRouter();
  const { id } = router.query;
  const [profile, setProfile] = useState<any>(null);

  const token = context && (context as any).token ? (context as any).token : null;

  useEffect(() => {
    if (typeof window !== "undefined" && id && token) {
      fetch(`http://localhost:8000/api/v1/users/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      })
        .then(res => res.json())
        .then(setProfile)
        .catch(err => console.error("Error fetching profile:", err));
    } else if (typeof window !== "undefined" && !token) {
       
    }
  }, [id, token]);

  if (!profile) return <p>Loading...</p>;

  return (
    <div>
      <h2>{profile.username}</h2>
      <p>{profile.email}</p>
    </div>
  );
}