import * as React from "react";
import { Grid } from "@material-ui/core";
import Header from "../Header";
import Card from "../Components/Card";
import axios from "axios";
import Pagination from "react-js-pagination";

export default function Home() {
  const [news, setNews] = React.useState([]);
  const [page, setPage] = React.useState(1);
  const [total, setTotal] = React.useState(0);
  React.useEffect(() => {
    axios.get("http://184.72.112.6:80/fetchNews?page=" + page).then((response) => {
      setNews(response.data.message);
      setTotal(response.data.total);
    });
  }, [page]);
  const handlePageChange = (pageNumberpaginate) => {
    console.log("pageNumberpaginate", pageNumberpaginate);
    setPage(pageNumberpaginate);
  };
  return (
    <>
      <Header />
      <Grid container spacing={2}>
        {news.length > 0
          ? news.map((newsInfo) => (
              <Grid key={newsInfo.id} item xs={12} sm={6} md={4}>
                <Card news={newsInfo} />
              </Grid>
            ))
          : null}
      </Grid>
      <div style={{ textAlign: "center" }}>
        <Pagination
          activePage={page}
          itemsCountPerPage={15}
          totalItemsCount={total}
          pageRangeDisplayed={5}
          onChange={handlePageChange}
        />
      </div>
    </>
  );
}
