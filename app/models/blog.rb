class Blog < ApplicationRecord
  belongs_to :user
  has_many :blog, dependent: :destroy
  has_many :favorites, dependent: :destroy

  def favorited_by?(user)
    favorites.where(user_id: user.id).exists?
  end
end
