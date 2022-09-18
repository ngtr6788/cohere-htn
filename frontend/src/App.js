import { useState } from "react";

function App() {
  const [pdfPath, setPdfPath] = useState("");
  const [keyword, setKeyword] = useState("");
  const [keywordsList, setKeywordsList] = useState([]);
  const [resultsList, setResultsList] = useState([]);

  const handleStateChange = (setState, event) => {
    setState(event.target.value);
  };

  const handleSubmit = () => {
    const bodyJSON = JSON.stringify({
      textPath: pdfPath,
      keywords: keywordsList,
    });

    fetch("http://127.0.0.1:5000/search", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: bodyJSON,
    })
      .then((response) => response.json())
      .then((resJSON) => setResultsList(resJSON.result));
  };

  const handleKeyword = () => {
    setKeywordsList([...keywordsList, keyword]);
    setKeyword("");
  };

  const handleClear = () => {
    setKeywordsList([]);
  };

  return (
    <>
      <p>Enter PDF path: </p>
      <input
        value={pdfPath}
        onChange={(e) => handleStateChange(setPdfPath, e)}
      />
      <p>{pdfPath}</p>
      <p>Add keyword: </p>
      <input
        value={keyword}
        onChange={(e) => handleStateChange(setKeyword, e)}
      />
      <button onClick={handleKeyword}>Add keyword</button>
      <button onClick={handleSubmit}>Find keywords</button>
      <button onClick={handleClear}>Clear keywords</button>
      {keywordsList && keywordsList.map((word) => <p>{word}</p>)}
      <h3>Results: </h3>
      {resultsList &&
        resultsList.map((result) => {
          return (
            <>
              <p>
                Page {result.pageNumber}: {result.text}{" "}
              </p>
            </>
          );
        })}
    </>
  );
}

export default App;
