interface LinkInputProps {
  setLink: (link: string) => void;
}

export default function LinkInput({ setLink }: LinkInputProps) {
  return (
    <div>
      <form
        className="flex flex-row gap-12"
        onSubmit={(e) => {
          e.preventDefault();
          const form = e.target as HTMLFormElement;
          const link = form.link.value;
          setLink(link);
        }}>
        <div className="w-full flex flex-col gap-2">
          <label className="text-white text-sm">Submit a RMP link</label>
          <input
            name="link"
            type="text"
            className="text-black rounded-lg p-2 w-full"
            placeholder="https://www.ratemyprofessors.com/professor/1"
          />
          <button
            type="submit"
            className="text-white bg-gray-800 px-4 py-1 rounded-lg hover:bg-gray-900 hover:duration-200">
            Get professor
          </button>
        </div>
      </form>
    </div>
  );
}
