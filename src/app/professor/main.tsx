"use client";

import QueryInput from "@/components/query-input";
import ProfessorList from "@/components/professor-list";
import { useState } from "react";

export default function MainPage() {
  const [query, setQuery] = useState("");

  return (
    <div className="px-24 pt-10">
      <QueryInput setQuery={setQuery} />
      <ProfessorList query={query} />
    </div>
  );
}
