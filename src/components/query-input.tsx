interface QueryInputProps {
  setQuery: (query: string) => void;
}

export default function QueryInput({ setQuery }: QueryInputProps) {
  return (
    <div>
      <form
        className="flex flex-row gap-12"
        onSubmit={(e) => {
          e.preventDefault();
          const form = e.target as HTMLFormElement;
          const query = form.query.value;
          setQuery(query);
        }}>
        <div className="w-full flex flex-col gap-2">
          <label className="text-white text-sm">Submit any query</label>
          <input
            name="query"
            type="text"
            className="text-black rounded-lg p-2 w-full"
            placeholder="Give me some professors"
          />
          <button
            type="submit"
            className="text-white bg-gray-800 px-4 py-1 rounded-lg hover:bg-gray-900 hover:duration-200">
            Query
          </button>
        </div>
      </form>
    </div>
  );
}
