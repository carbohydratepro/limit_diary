60.times do |n|
  Blog.create!(
    title: Faker::Book.title,
    body: "初の投稿です。よろしくお願いします！",
    user_id: 1,
  )
end
