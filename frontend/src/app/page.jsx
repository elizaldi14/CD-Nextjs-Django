import FormTask from "./components/FormTask";
import ListTask from "./components/ListTask";

export const dynamic = "force-dynamic";

function Homepage() {
  return (
    <div className="container mx-auto">
      <h1 className="mb-5"> Task App</h1>

      <div className="flex gap-x-10">

        <FormTask />

        <ListTask />

      </div>
    </div>
  );
}

export default Homepage;
