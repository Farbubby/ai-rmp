"use client";

import QueryInput from "@/components/query-input";
import ProfessorList from "@/components/professor-list";
import Navbar from "@/components/navbar";
import { useState } from "react";

export default function MainPage() {
  const [query, setQuery] = useState("");
  const [page, setPage] = useState("Enter a query");

  return (
    <>
      <Navbar page={page} setPage={setPage} />
      {page === "Enter a query" ? (
        <div className="px-12 pt-28 pb-28">
          <QueryInput setQuery={setQuery} />
          <ProfessorList query={query} />
        </div>
      ) : null}
      {page === "Submit a link" ? (
        <div className="px-12 pt-28 pb-28 text-white">Submit a link</div>
      ) : null}
    </>
  );
}
