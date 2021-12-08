CREATE TABLE IF NOT EXISTS public."videocategory"
(
    id serial NOT NULL,
    video_id character varying,
    video_category_id character varying,
    channel_name character varying,
    channel_id character varying,
    PRIMARY KEY (id)
);

ALTER TABLE public."videocategory"
    OWNER to postgres_a;
