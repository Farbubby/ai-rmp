"use client";

import { useQuery } from "@tanstack/react-query";
import ProfessorInfo from "./professor-info";

interface LinkProfessorProps {
  link: string;
}

export default function LinkProfessor({ link }: LinkProfessorProps) {
  const state = useQuery({
    queryKey: ["professor", link],
    queryFn: ({ queryKey }) =>
      fetch(`/api/link`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ link: queryKey[1] }),
      }).then(
        (res) =>
          res.json() as Promise<{
            prof_name: string;
            prof_dept: string;
            num_ratings: string;
            difficulty: string;
            rating: string;
            summary: string;
            top_tags: string[];
            university_name: string;
            would_take_again: string;
            comments: string[];
            classes_taught: string[];
          }>
      ),
  });

  if (!link) {
    return (
      <div className="text-white w-full flex flex-row justify-center mt-24">
        <div>Enter a RMP link to get information on your professor!</div>
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

  return (
    <>
      <div className="text-white mt-24">
        <div className="flex flex-col gap-8">
          <div className="text-4xl">{state.data.prof_name}</div>
          <ProfessorInfo
            rating={state.data.rating}
            difficulty={state.data.difficulty}
            numRatings="0"
            department={state.data.prof_dept}
            university={state.data.university_name}
            classesTaught={state.data.classes_taught}
            topTags={state.data.top_tags}
            takeAgain="0%"
            summary={state.data.summary}
          />
        </div>
      </div>
    </>
  );
}
