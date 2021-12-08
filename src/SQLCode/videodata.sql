CREATE TABLE IF NOT EXISTS public."videodata"
(
    id serial NOT NULL,
    channel_name text,
    channel_id character varying,
    video_id character varying,
    published_at character varying,
    title text,
    description text,
    PRIMARY KEY (id)
);
