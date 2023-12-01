import { useEffect, useRef, useState } from "react";
import { analizeCode } from "../api";

const Analizer = ({ setResult }) => {
  const [code, setCode] = useState("");
  const linesRef = useRef();
  const textAreaRef = useRef();
  const handleChange = (ev) => {
    setCode(ev.target.value);
  };

  const sendCode = async () => {
    const result = await analizeCode(code);
    setResult(result);
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

    const textareaStyles = window.getComputedStyle(textAreaRef?.current);
    [
      "fontFamily",
      "fontSize",
      "fontWeight",
      "letterSpacing",
      "lineHeight",
      "padding",
    ].forEach((property) => {
        linesRef.current.style[property] = textareaStyles[property];
    });
  }, [code]);

  return (
    <div className="input">
      <div className="analizerContainer">
        <div ref={linesRef} className="lines" />
        <textarea
          ref={textAreaRef}
          className="analizerArea"
          value={code}
          onChange={handleChange}
        />
      </div>
      <button className="analize-button" onClick={sendCode}>
        {" "}
        Analizar{" "}
      </button>
    </div>
  );
};

export default Analizer;
