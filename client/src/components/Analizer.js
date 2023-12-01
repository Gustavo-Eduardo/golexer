import { useEffect, useRef, useState } from "react";

const Analizer = () => {
  const [code, setCode] = useState("");
  const linesRef = useRef();
  const textAreaRef = useRef();
  const handleChange = (ev) => {
    setCode(ev.target.value);
  };
  useEffect(() => {
    const lines = textAreaRef?.current?.value?.split("\n");
    if (linesRef.current) {
      linesRef.current.innerHTML = Array.from(
        {
          length: lines.length,
        },
        (_, i) => `<div>${i + 1}</div>`
      ).join("");
    }
  }, [code]);

  return (
    <div>
      <div className="analizerContainer">
        <div ref={linesRef} className="lines" />
        <textarea
          ref={textAreaRef}
          className="analizerArea"
          value={code}
          onChange={handleChange}
        />
      </div>
      <button className="analize-button"> Analize </button>
    </div>
  );
};

export default Analizer;
