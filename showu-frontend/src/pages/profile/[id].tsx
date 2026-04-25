// src/pages/profile/[id].tsx

import { useContext, useEffect, useState } from "react";
import { AuthContext } from "../../context/AuthContext";
import { useRouter } from "next/router";

export default function ProfilePage() {
  
  const auth = useContext(AuthContext); 
  const router = useRouter();
  const { id } = router.query;
  const [profile, setProfile] = useState<any>(null);

  useEffect(() => {
    if (!auth || !auth.token) {
      if (typeof window !== "undefined") {
        router.push("/login");
      }
      return;
    }
    
    fetch(`http://localhost:8000/api/v1/users/${id}`, {
      headers: { Authorization: `Bearer ${auth.token}` },
    })
      .then(res => res.json())
      .then(setProfile);
  }, [id, auth, router]);

  if (!profile) return <p>Loading...</p>;

  return (
    <div>
      <h2>{profile.username}</h2>
      <p>{profile.email}</p>
    </div>
  );
}