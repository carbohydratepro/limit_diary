require "csv"

CSV.foreach('db/users.csv').with_index do |row, index|
  User.create(:name => row[0], :password => row[1], :email => row[2], :introduction => row[3], :created_at => row[4], :updated_at => row[5], :image => File.open("./app/assets/images/icon_#{index}.png"))
end

CSV.foreach('db/blogs.csv').with_index do |row, index|
  Blog.create(:title => row[0], :body => row[1], :user_id => row[2], :created_at => row[3], :updated_at => row[4])
end
