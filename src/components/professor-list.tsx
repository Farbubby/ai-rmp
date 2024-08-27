"use client";

import { useQuery } from "@tanstack/react-query";
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from "@/components/ui/accordion";
import ProfessorInfo from "./professor-info";

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

  const professors = (
    <Accordion type="single" collapsible className="mt-24">
      {state.data.map((professor, index) => {
        return (
          <>
            <AccordionItem value={`item-${index}`}>
              <AccordionTrigger>{professor.id}</AccordionTrigger>
              <AccordionContent>
                <ProfessorInfo
                  rating={professor.metadata.rating}
                  difficulty={professor.metadata.difficulty}
                  numRatings="0"
                  department={professor.metadata.department}
                  university={professor.metadata.university}
                  classesTaught={professor.metadata.classes_taught}
                  topTags={professor.metadata.top_tags}
                  takeAgain="0%"
                />
              </AccordionContent>
            </AccordionItem>
          </>
        );
      })}
    </Accordion>
  );

  return (
    <>
      <div className="text-white">{professors}</div>
    </>
  );
}
