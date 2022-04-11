import { useEffect, useState } from "react";
import axios from "axios";

const APICompany = () => {
  const [Apidata, setApidata] = useState([]);

  useEffect(() => {
    const Company_data = async () => {
      // const url = "https://f339-2405-201-3021-9843-455d-8160-fba8-b9e1.ngrok.io/api/company/";
      const url =
        "https://f339-2405-201-3021-9843-455d-8160-fba8-b9e1.ngrok.io/api/company/";

      const response = await axios.get(url);
      console.log(response.data);
      setApidata(response.data);
    };
    Company_data();
  }, []);

  return Apidata.map((postinfo) => (
    <div key={postinfo.id} className="post">
      {postinfo.id}
      <br></br>
      <b>{postinfo.title}</b>
      <br></br>
      {postinfo.body}
    </div>
  ));
};

export default APICompany;
