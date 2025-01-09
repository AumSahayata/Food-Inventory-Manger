import { SignUp } from "@clerk/nextjs";

const signup = () => {
  return (
    <>
      <div className="flex justify-center items-center h-full w-full">
        <SignUp />
      </div>
    </>
  );
};

export default signup;
