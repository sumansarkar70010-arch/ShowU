// src/pages/login.tsx

import { useContext, useState } from "react";
import { AuthContext } from "../context/AuthContext";

export default function LoginPage() {
  // ১. সরাসরি { login } না লিখে পুরো context টি নিরাপদভাবে চেক করা হচ্ছে
  const auth = useContext(AuthContext);
  const login = auth ? auth.login : null;

  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async (e: any) => {
    e.preventDefault();
    // ২. লগইন ফাংশনটি আছে কি না চেক করে কল করা
    if (login) {
      await login(email, password);
    } else {
      console.error("Login function is not available");
    }
  };

  return (
    <div className="auth-form">
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <input type="email" placeholder="Email" value={email} onChange={e => setEmail(e.target.value)} />
        <input type="password" placeholder="Password" value={password} onChange={e => setPassword(e.target.value)} />
        <button type="submit">Login</button>
      </form>
    </div>
  );
}