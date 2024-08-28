"use client";

import QueryInput from "@/components/query-input";
import LinkInput from "@/components/link-input";
import QueryProfessors from "@/components/query-professors";
import LinkProfessor from "@/components/link-professor";
import Navbar from "@/components/navbar";
import { useState } from "react";

export default function MainPage() {
  const [query, setQuery] = useState("");
  const [link, setLink] = useState("");
  const [page, setPage] = useState("Enter a query");

  return (
    <>
      <Navbar page={page} setPage={setPage} />
      {page === "Enter a query" ? (
        <div className="px-12 pt-28 pb-28">
          <QueryInput setQuery={setQuery} />
          <QueryProfessors query={query} />
        </div>
      ) : null}
      {page === "Submit a link" ? (
        <div className="px-12 pt-28 pb-28">
          <LinkInput setLink={setLink} />
          <LinkProfessor link={link} />
        </div>
      ) : null}
    </>
  );
}
