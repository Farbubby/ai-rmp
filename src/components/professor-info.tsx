interface ProfessorInfoProps {
  rating: string;
  difficulty: string;
  numRatings: string;
  department: string;
  university: string;
  classesTaught: string[];
  topTags: string[];
  takeAgain: string;
  summary: string;
}

export default function ProfessorInfo({
  rating,
  difficulty,
  numRatings,
  department,
  university,
  classesTaught,
  topTags,
  takeAgain,
  summary,
}: ProfessorInfoProps) {
  return (
    <>
      <div className="flex flex-col gap-4">
        <div>
          <div className="text-sm text-white">
            Overall Rating (Out of{" "}
            <span className="text-orange-400">{numRatings}</span> ratings)
          </div>{" "}
          <div className="text-orange-400 text-lg">{rating} </div>
        </div>
        <div>
          <div className="text-sm text-white">Department</div>{" "}
          <div className="text-orange-400 text-lg">{department}</div>
        </div>
        <div>
          <div className="text-sm text-white">University</div>{" "}
          <div className="text-orange-400 text-lg">{university}</div>
        </div>
        <div>
          <div className="text-sm text-white">Difficulty</div>{" "}
          <div className="text-orange-400 text-lg">{difficulty}</div>
        </div>
        <div className="text-white text-xl">
          <div className="text-sm text-white">Classes taught before:</div>{" "}
          <div className="text-orange-400 text-lg">
            {classesTaught.join(", ")}
          </div>
        </div>
        <div className="text-white text-xl">
          <div className="text-sm text-white">Considerations:</div>{" "}
          <div className="text-orange-400 text-lg">{topTags.join(", ")}</div>
        </div>
        <div className="text-white text-xl">
          <div className="text-sm text-white">Would take again?</div>
          <div className="text-orange-400 text-lg">{takeAgain}</div>
        </div>
        <div className="text-sm">{summary}</div>
      </div>
    </>
  );
}
