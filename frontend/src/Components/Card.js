import * as React from "react";
import { Link } from "react-router-dom";
import Box from "@material-ui/core/Box";

import {
  Card,
  CardActionArea,
  CardContent,
  Typography,
} from "@material-ui/core";

export default function Cards(props) {
  const [title, setTitle] = React.useState();
  const [summary, setSummary] = React.useState();
  const [link, setLink] = React.useState();
  const [sentiment, setsentiment] = React.useState();
  React.useEffect(() => {
    setTitle(props.news.Article_Title);
    setSummary(props.news.Article_Summary);
    setLink(props.news.link);
    setsentiment(props.news.sentiment);
  }, []);
  return (
    <Card>
      <CardActionArea>
        <a href={link} target="_blank" style={{ textDecoration: "none" }}>
          <CardContent>
            <Typography gutterBottom variant="h5" component="h2">
              {title}
            </Typography>
            <div style={{ display: "flex" }}>
              <Typography
                variant="body2"
                color="dark"
                component="p"
                style={{ color: "black", fontWeight: "600" }}
              >
                Sentiment:{" "}
              </Typography>
              <Typography variant="body2" color="secondary" component="p">
                {" "}
                {sentiment}
              </Typography>
            </div>
            <Typography variant="body2" color="textSecondary" component="p">
              {summary}
            </Typography>
          </CardContent>
        </a>
      </CardActionArea>
    </Card>
  );
}
