import { bcrypt, Drash } from "../../deps.ts";
import ArticleCommentsResource from "../../resources/article_comments_resource.ts";
import ArticlesResource from "../../resources/articles_resource.ts";
import HomeResource from "../../resources/home_resource.ts";
import ProfilesResource from "../../resources/profiles_resource.ts";
import TagsResource from "../../resources/tags_resource.ts";
import UserResource from "../../resources/user_resource.ts";
import UsersLoginResource from "../../resources/users_login_resource.ts";
import UsersResource from "../../resources/users_resource.ts";
import type { ArticleEntity } from "../../models/article_model.ts";
import BaseModel from "../../models/base_model.ts";
import type { QueryResult } from "../../deps.ts";
import { ArticleCommentEntity } from "../../models/article_comments_model.ts";

// TODO(edward) Add docblocks

export function createServerObject(): Drash.Http.Server {
  const server = new Drash.Http.Server({
    directory: ".",
    response_output: "application/json",
    resources: [
      ArticleCommentsResource,
      ArticlesResource,
      HomeResource,
      ProfilesResource,
      TagsResource,
      UserResource,
      UsersLoginResource,
      UsersResource,
    ],
    views_path: "./public/views",
  });
  return server;
}

export async function createTestArticle(overrides?: ArticleEntity) {
  const query =
    `INSERT INTO articles (author_id, title, description, body, slug, created_at, updated_at, tags) VALUES($1, $2, $3, $4, $5, to_timestamp($6), to_timestamp($7), $8);`;
  await BaseModel.query(query, overrides && overrides.author_id ? overrides!.author_id : 1,
      overrides && overrides!.title ? overrides!.title : "Test Article Title",
      overrides && overrides!.description
          ? overrides!.description
          : "Test Article Description",
      overrides && overrides!.body ? overrides!.body : "Test Article Body",
      overrides && overrides!.slug ? overrides!.slug : "test-article-title",
      String(Date.now() / 100.00),
      String(Date.now() / 100.00),
      overrides && overrides!.tags ? overrides!.tags : "",);
  const title = overrides && overrides!.title
    ? overrides!.title
    : "Test Article Title";
  const result = await BaseModel.query(
    `SELECT * FROM articles WHERE title = '${title}' LIMIT 1;`,
  );
  return result.rows[0];
}

export async function clearTestArticles() {
  const query = "DELETE FROM articles";
  await BaseModel.query(query);
}

export async function createTestComment(overrides: {
  article_id?: number;
  author_image?: string;
  author_id?: number;
  author_username?: string;
  body?: string;
} = {}) {
  const query =
    `INSERT INTO article_comments (article_id, author_image, author_id, author_username, body, created_at, updated_at) VALUES ($1, $2, $3, $4, $5, to_timestamp($6), to_timestamp($7));`;
  await BaseModel.query(query, overrides!.article_id ? `${overrides!.article_id}` : 1,
      overrides!.author_image
          ? overrides!.author_image
          : "https://static.productionready.io/images/smiley-cyrus.jpg",
      overrides!.author_id ? overrides!.author_id : 1,
      overrides!.author_username ? overrides!.author_username : "Test Username",
      overrides!.body ? overrides!.body : "Test Body",
      String(Date.now()),
      String(Date.now()),);
  const body = overrides && overrides!.body ? overrides!.body : "Test Body";
  const result = await BaseModel.query(
    `SELECT * FROM article_comments WHERE body = '${body}' LIMIT 1;`,
  );
  return result.rows[0];
}

export async function clearTestComments() {
  const query = "DELETE FROM article_comments";
  await BaseModel.query(query);
}

export async function createTestSession(overrides: {
  user_id?: number;
  session_one?: string;
  session_two?: string;
} = {}) {
  const query =
    `INSERT INTO sessions (user_id, session_one, session_two) VALUES($1, $2, $3);`;
  await BaseModel.query(query, overrides && overrides.user_id ? overrides.user_id : 1,
      overrides && overrides.session_one
          ? overrides.session_one
          : "Test Session 1",
      overrides && overrides.session_two ? overrides.session_two
          : "Test Session 2",);
  const userId = overrides && overrides.user_id ? overrides.user_id : 1;
  const result = await BaseModel.query(
    `SELECT * FROM sessions WHERE user_id = '${userId}' LIMIT 1;`,
  );
  return result.rows[0];
}

export async function clearTestSessions() {
  const query = "DELETE FROM sessions";
  await BaseModel.query(query);
}

export async function createTestUser(overrides: {
  username?: string;
  password?: string;
  email?: string;
  image?: string;
  bio?: string;
} = {}) {
  const query =
    `INSERT INTO users (username, password, email, created_on, last_login, image, bio) VALUES($1, $2, $3, to_timestamp($4), to_timestamp($5), $6, $7);`;
  await BaseModel.query(query, overrides && overrides.username ? overrides.username : "testUsername",
      overrides && overrides.password
          ? await bcrypt.hash(overrides.password)
          : await bcrypt.hash("TestPassword1"),
      overrides && overrides.email ? overrides.email : "test@hotmail.com",
      String(Date.now() / 100.00),
      String(Date.now() / 100.00),
      overrides && overrides.image ? overrides.image
          : "https://static.productionready.io/images/smiley-cyrus.jpg",
      overrides && overrides.bio ? overrides.bio : "Test bio",);
  const username = overrides && overrides.username
    ? overrides.username
    : "testUsername";
  const result = await BaseModel.query(
    `SELECT * FROM users WHERE username = '${username}' LIMIT 1;`,
  );
  return result.rows[0];
}

export async function clearTestUsers(username?: string) {
  username = username ? username : "testUsername";
  let query = `SELECT * FROM users WHERE username = '${username}'`;
  const result = await BaseModel.query(query);
  const id = result.rows.length ? result.rows[0]["id"] : 0;
  console.log('clearing test user. Here is idd: ' + id)
  if (id) {
    query = `DELETE FROM sessions WHERE user_id =  ${id}`;
    await BaseModel.query(query);
  }
  await BaseModel.query(`DELETE FROM users WHERE username = '${username}'`);
}
