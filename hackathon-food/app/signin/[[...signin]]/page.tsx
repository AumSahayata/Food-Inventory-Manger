import { SignIn } from "@clerk/nextjs";

const signin = () => {
  return (
    <>
      <div className="flex justify-center items-center w-full h-full">
        <SignIn />
      </div>
    </>
  );
};

export default signin;
