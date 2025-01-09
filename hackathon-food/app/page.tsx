import { SignedIn, UserButton } from "@clerk/nextjs";
import { currentUser } from "@clerk/nextjs/server";

import Dashboard from "./components/dashboard";

export default async function Home() {
  const user = await currentUser();

  return (
    <>
      <Dashboard />
    </>
  );
}
