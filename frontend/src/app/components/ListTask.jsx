import TaskCard from "./TaskCard";


async function loadTask() {
    const res = await fetch(`${process.env.NEXT_PUBLIC_BACKEND_URL}/api/tasks/`);
    const tasks = await res.json();
    return tasks;
  }




async function ListTask() {
    
    const tasks = await loadTask()

    console.log(tasks)
    
    return(

        <div className="bg-slate-600 p-4 w-full">
            <h1>List Task</h1>

            {tasks.map(task =>(
               <TaskCard task={task} key={task.id} className="bg-slate-500 px-4 py-3 mb-2 rounded-md flex justify-between items-center" />
            ))}

        </div>
    )
}

export default ListTask