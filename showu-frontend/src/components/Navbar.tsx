// src/components/Navbar.tsx

import Link from "next/link";
import React from "react";

export default function Navbar():React.ReactElement {
  return (
    <nav className="navbar" aria-label="Main navigation">
      <ul className="navbar-list">
        <li><Link href="/">🏠 Home</Link></li>
        <li><Link href="/upload">➕ Upload</Link></li>
        <li><Link href="/profile">👤 Profile</Link></li>
        <li><Link href="/analytics">📊 Analytics</Link></li>
      </ul>
    </nav>
  );
}