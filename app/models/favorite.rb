class Favorite < ApplicationRecord
  belongs_to :user
  belongs_to :blog

  validates_uniqueness_of :blog_id, scope: :user_id
end
