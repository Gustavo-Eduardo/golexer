import { useState } from "react";
import Analizer from "./Analizer";
import Result from "./Result";

const CodeAnalizer = () => {
  const [result, setResult] = useState(null);

  return (
    <div className="container">
      <Analizer setResult={setResult}/>
      <Result result={result}/>
    </div>
  );
};

export default CodeAnalizer;
