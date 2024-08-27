"use client";

import { useQuery } from "@tanstack/react-query";

interface ProfessorListProps {
  query: string;
}

export default function ProfessorList({ query }: ProfessorListProps) {
  const state = useQuery({
    queryKey: ["professors", query],
    queryFn: ({ queryKey }) =>
      fetch(`http://localhost:5000/api/professors?query=${queryKey[1]}`).then(
        (res) =>
          res.json() as Promise<
            {
              id: string;
              metadata: {
                classes_taught: string[];
                department: string;
                difficulty: string;
                rating: string;
                summary: string;
                top_tags: string[];
                university: string;
              };
            }[]
          >
      ),
  });

  if (!query) {
    return (
      <div className="text-white w-full flex flex-row justify-center mt-24">
        <div>Enter something to find professor recommendations!</div>
      </div>
    );
  }

  if (state.isLoading) {
    return (
      <div className="text-white w-full flex flex-row justify-center mt-24">
        <div>Loading...</div>
      </div>
    );
  }

  if (state.isError) {
    return (
      <div className="text-white w-full flex flex-row justify-center mt-24">
        <div>Error: {state.error.message}</div>
      </div>
    );
  }

  if (!state.data) {
    return (
      <div className="text-white w-full flex flex-row justify-center mt-24">
        <div>No data found</div>
      </div>
    );
  }

  if (state.data.length === 0) {
    return (
      <div className="text-white w-full flex flex-row justify-center mt-24">
        <div>No professors found</div>
      </div>
    );
  }

  const professors = state.data.map((professor) => {
    return (
      <div key={professor.id} className="w-full flex flex-row gap-4 mt-4">
        <div className="w-1/2">
          <div className="text-white text-lg">{professor.id}</div>
          <div className="text-white text-sm">{professor.metadata.rating}</div>
        </div>
        <div className="w-1/2">
          <div className="text-white text-sm">
            {professor.metadata.department}
          </div>
          <div className="text-white text-sm">
            {professor.metadata.university}
          </div>
        </div>
      </div>
    );
  });

  return (
    <>
      <div className="text-white">{professors}</div>
    </>
  );
}
