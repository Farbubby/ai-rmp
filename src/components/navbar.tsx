interface NavbarProps {
  page: string;
  setPage: (page: string) => void;
}

export default function Navbar({ page, setPage }: NavbarProps) {
  const q = page === "Enter a query" ? "bg-gray-700 duration-200" : "";
  const s = page === "Submit a link" ? "bg-gray-700 duration-200" : "";

  return (
    <>
      <div className="bg-gray-900 w-fit fixed top-5 left-5 py-2 px-4 rounded-lg text-white flex flex-row gap-4 items-center">
        <button
          onClick={() => {
            setPage("Enter a query");
          }}>
          <div className={"py-1 px-2 rounded-lg " + q}>Enter a query</div>
        </button>
        <div>|</div>
        <button
          onClick={() => {
            setPage("Submit a link");
          }}>
          <div className={"py-1 px-2 rounded-lg " + s}>Submit a link</div>
        </button>
      </div>
    </>
  );
}
